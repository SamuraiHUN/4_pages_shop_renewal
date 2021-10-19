search this:

		else if (!stricmp(pszFlag, "ltr"))
			pWin->RemoveFlag(UI::CWindow::FLAG_RTL);


add under this:

		else if (!stricmp(pszFlag, "window_without_alpha"))
			pWin->AddFlag(UI::CWindow::FLAG_IS_BOARD_WITHOUT_ALPHA);