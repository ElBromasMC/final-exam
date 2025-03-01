
NODEBIN ?= ./node_modules/.bin
TAILWINDCSS_OUT := ./src/static/css/tailwind.css

$(TAILWINDCSS_OUT): ./src/index.html tailwind.config.cjs tailwind.css
	"$(NODEBIN)/tailwindcss" build -i tailwind.css -o "$(TAILWINDCSS_OUT)" --watch=always &
	"$(NODEBIN)/tailwindcss" build -i tailwind.css -o "$@" --minify
	touch "$@"

.PHONY: start
start: $(TAILWINDCSS_OUT)
	cd ./src && python ./server.py -v

.PHONY: clean
clean:
	rm -f "$(TAILWINDCSS_OUT)"

.SECONDARY:
