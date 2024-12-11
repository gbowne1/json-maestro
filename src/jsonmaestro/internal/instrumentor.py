from io import TextIOWrapper
import json
import time
import threading

from typing import Union


class ProfileResult:
	name: str
	start: int
	end: int
	thread_id: int

	def __init__(self, name: str, start: int, end: int,
	             thread_id: int) -> None:
		self.name = name
		self.start = start
		self.end = end
		self.thread_id = thread_id


class InstrumentationSession:
	name: str

	def __init__(self, name: str):
		self.name = name


class Instrumentor:
	_instance = None
	current_session: Union[InstrumentationSession, None]
	output_stream: Union[TextIOWrapper, None]

	def __init__(self):
		self.current_session = None
		self.output_stream = None
		self.profile_count = 0

	def begin_session(self, name: str, filepath: str = "results.json"):
		self.output_stream = open(filepath, "w")
		self._write_header()
		self.current_session = InstrumentationSession(name)

	def end_session(self):
		self._write_footer()
		if self.output_stream is not None:
			self.output_stream.close()
		self.current_session = None
		self.profile_count = 0

	def write_profile(self, result: ProfileResult):
		if self.profile_count > 0:
			if self.output_stream is not None:
				self.output_stream.write(",")

		profile_data = {
		    "cat": "function",
		    "dur": result.end - result.start,
		    "name": result.name.replace('"', "'"),
		    "ph": "X",
		    "pid": 0,
		    "tid": result.thread_id,
		    "ts": result.start
		}
		if self.output_stream is not None:
			self.output_stream.write(json.dumps(profile_data))
			self.output_stream.flush()

		self.profile_count += 1

	def _write_header(self):
		if self.output_stream is not None:
			self.output_stream.write("{\"otherData\": {},\"traceEvents\":[")
			self.output_stream.flush()

	def _write_footer(self):
		if self.output_stream is not None:
			self.output_stream.write("]}")
			self.output_stream.flush()

	@staticmethod
	def get():
		if Instrumentor._instance is None:
			Instrumentor._instance = Instrumentor()
			# return None
		return Instrumentor._instance


class InstrumentationTimer:
	name: str
	stopped: bool

	def __init__(self, name: str):
		self.name = name
		self.start_timepoint = time.time()
		self.stopped = False

	def stop(self):
		if self.stopped:
			return

		end_timepoint = time.time()
		start = int(self.start_timepoint *
		            1_000_000)  # Convert to microseconds
		end = int(end_timepoint * 1_000_000)  # Convert to microseconds
		thread_id = threading.get_ident()

		instrumentor = Instrumentor.get()
		if instrumentor:
			instrumentor.write_profile(
			    ProfileResult(self.name, start, end, thread_id))
		self.stopped = True

	def __del__(self):
		if not self.stopped:
			self.stop()

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		self.stop()


# Example Usage:
if __name__ == "__main__":
	Instrumentor.get().begin_session("Example Session")

	with InstrumentationTimer("Example Scope"):
		time.sleep(0.5)  # Simulating work
		with InstrumentationTimer(name="new-scope1"):
			time.sleep(0.25)  # Simulating work
		with InstrumentationTimer(name="new-scope2"):
			time.sleep(0.25)  # Simulating work

	Instrumentor.get().end_session()
