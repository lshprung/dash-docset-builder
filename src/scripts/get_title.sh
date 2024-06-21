get_title() {
	pup -p -f "$1" 'title text{}' | \
		tr -d \\n | \
		sed 's/\"/\"\"/g'
}
