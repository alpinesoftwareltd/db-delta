

PHONY: build-test-image
build-test-image:
	docker pull python:3.12

	docker build -t db-delta-test -f Dockerfile.test .

PHONY: run-test-image
run-test-image: build-test-image
	docker run --rm db-delta-test

PHONY: build-artifact
build-artifact: run-test-image
	docker pull python:3.12

	docker build \
		-t db-delta-build \
		-f Dockerfile.build \
		.
	docker run \
		-e TWINE_USERNAME=__token__ \
		-e TWINE_PASSWORD=${PYPI_TOKEN} \
		--rm db-delta-build
