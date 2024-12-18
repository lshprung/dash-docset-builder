#!/usr/bin/env sh

#DEBUG="yes"

# shellcheck source=../create_table.sh
. "$(dirname "$0")"/../create_table.sh
# shellcheck source=../insert.sh
. "$(dirname "$0")"/../insert.sh

TYPE="$1"
shift
INDEX_ENTRY_CLASS="$1"
shift
DB_PATH="$1"
shift

insert_index_terms() {
	# Get each term from an index page and insert
	while [ -n "$1" ]; do
		grep -Eo "class=${INDEX_ENTRY_CLASS}.*<a href.*</a>" "$1" | while read -r line; do
			insert_term "$line"
		done

		shift
	done
}

insert_term() {
	LINK="$1"
	NAME="$(echo "$LINK" | pup -p 'a text{}' | sed 's/"/\"\"/g' | head -n 1)"
	PAGE_PATH="$(echo "$LINK" | pup -p 'a attr{href}' | head -n 1)"

	if [ -n "$DEBUG" ]; then
		echo "LINK is $LINK" >> /dev/stderr
		echo "          vanilla NAME is $(echo "$LINK")" >> /dev/stderr
		echo "01 transformation NAME is $(echo "$LINK" | pup -p 'a text{}')" >> /dev/stderr
		echo "02 transformation NAME is $(echo "$LINK" | pup -p 'a text{}' | sed 's/"/\"\"/g')" >> /dev/stderr
		echo "            final NAME is $(echo "$LINK" | pup -p 'a text{}' | sed 's/"/\"\"/g' | head -n 1)" >> /dev/stderr
		echo "           vanilla PAGE_PATH is $(echo "$LINK")" >> /dev/stderr
		echo "01 trainsformation PAGE_PATH is $(echo "$LINK" | pup -p 'a attr{href}')" >> /dev/stderr
		echo "             final PAGE_PATH is $(echo "$LINK" | pup -p 'a attr{href}' | head -n 1)" >> /dev/stderr
		echo >> /dev/stderr
	fi

	insert "$DB_PATH" "$NAME" "$TYPE" "$PAGE_PATH"
}

create_table "$DB_PATH"
insert_index_terms "$@"
