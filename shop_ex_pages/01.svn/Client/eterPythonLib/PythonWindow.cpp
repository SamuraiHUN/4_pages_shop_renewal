Search this:

		if (IsFlag(CWindow::FLAG_NOT_PICK))
			return NULL;

add under this:

		if (IsFlag(CWindow::FLAG_IS_BOARD_WITHOUT_ALPHA)) // check flag
		{
			return NULL;
		}