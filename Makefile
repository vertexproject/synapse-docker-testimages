RELEASE = 3.6.1.a1

all: test

build:
	docker build -t synapse_test_image:$(RELEASE) .

test:
	docker run synapse_test_image:$(RELEASE) python -c 'import msgpack'
	docker run synapse_test_image:$(RELEASE) python -c 'import psycopg2'
	docker run synapse_test_image:$(RELEASE) python -c 'import cryptography'
	docker run synapse_test_image:$(RELEASE) python -c 'import tornado'
