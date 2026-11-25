.PHONY: test test-python test-java test-js clean

test: test-python test-java test-js

test-python:
	python3 -m pytest spot_the_vuln/python coding_round -q

test-java:
	@set -e; for d in spot_the_vuln/java/*/; do \
		cls=$$(basename $$d*Check.java .java); \
		out=build/$$(basename $$d); \
		mkdir -p $$out; \
		javac -d $$out $$d*.java; \
		echo "== $$d"; \
		java -cp $$out $$cls; \
	done

test-js:
	@set -e; for d in spot_the_vuln/javascript/*/; do \
		echo "== $$d"; \
		node --test $$d*.test.js; \
	done

clean:
	rm -rf build .pytest_cache
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
