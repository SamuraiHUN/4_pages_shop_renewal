in class Button(Window):

search this:

	def SetTextColor(self, color):
		if not self.ButtonText:
			return
		self.ButtonText.SetPackedFontColor(color)

add under this:

	def SetTextPosition(self, x, y):
		self.ButtonText.SetPosition(x, y)
		self.ButtonText.SetWindowHorizontalAlignCenter()
		self.ButtonText.SetWindowVerticalAlignCenter()

in class RadioButtonGroup:

search this:

	def SetText(self, idx, text):
		if idx >= len(self.buttonGroup):
			return
		(button, selectEvent, unselectEvent) = self.buttonGroup[idx]
		button.SetText(text)

add under this:

	def SetTextPosition(self, idx, x, y):
		if idx >= len(self.buttonGroup):
			return
		(button, selectEvent, unselectEvent) = self.buttonGroup[idx]
		button.SetTextPosition(x, y)
	
	def SetToolTipText(self, idx, text):
		if idx >= len(self.buttonGroup):
			return
		(button, selectEvent, unselectEvent) = self.buttonGroup[idx]
		button.SetToolTipText(text)

in def LoadElementButton

search this:

			if value.has_key("text_color"):
				window.SetTextColor(value["text_color"])

add under this:

		if True == value.has_key("tooltip_text"):
			if True == value.has_key("tooltip_x") and True == value.has_key("tooltip_y"):
				window.SetToolTipText(value["tooltip_text"], int(value["tooltip_x"]), int(value["tooltip_y"]))
			else:
				window.SetToolTipText(value["tooltip_text"])

again:

			if value.has_key("text_color"):
				window.SetTextColor(value["text_color"])

add before:

			if True == value.has_key("text_x") and True == value.has_key("text_y"):
				window.SetTextPosition(value["text_x"], value["text_y"])
				
search this:

	def OnClick(self, btnIdx):
	
replace the function with:

	def OnClick(self, btnIdx):
		if btnIdx == self.selectedBtnIdx:
			return
		(button, selectEvent, unselectEvent) = self.buttonGroup[self.selectedBtnIdx]
		if unselectEvent:
			unselectEvent(self.selectedBtnIdx)
		button.SetUp()

		self.selectedBtnIdx = btnIdx
		(button, selectEvent, unselectEvent) = self.buttonGroup[btnIdx]
		if selectEvent:
			selectEvent(btnIdx)

		button.Down()