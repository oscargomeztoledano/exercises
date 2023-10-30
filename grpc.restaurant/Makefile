#

STUBS = restaurant_pb2.py restaurant_pb2_grpc.py

all: $(STUBS)

%_pb2.py: %.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. $<


clean:
	$(RM) *~ $(STUBS)
	$(RM) -r __pycache__
