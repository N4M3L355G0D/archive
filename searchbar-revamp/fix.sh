find resources/ -iname "*.pdf" | sed s\|^\|"rm \""\|g | sed s\|"$"\|"\""\|g | bash
