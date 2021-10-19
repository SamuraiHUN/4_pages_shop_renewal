search this:

	def __ShowSmallTabs(self):
		self.smallRadioButtonGroup.Show()

add under this:

	#########################################
	#########################################
	def __ShowReworkedShopTabs(self):
		if self.reworkedRadioButtonGroup:
			self.reworkedRadioButtonGroup.Show()

	def __HideReworkedShopTabs(self):
		if self.reworkedRadioButtonGroup:
			self.reworkedRadioButtonGroup.Hide()
	
	def __CreateReworkedShopButtons(self, groupSize):
		def __GetButtonX(buttonIndex, width):
			CENTER_X = (self.GetWidth()/2) + (2 if groupSize != 1 else 0)
			realgroupSize = groupSize-1
			return CENTER_X - (int(width/2) - (int(width/2 * realgroupSize)) + (((realgroupSize) - buttonIndex) * width))
		
		self.reworkedRadioButtonGroup = ui.RadioButtonGroup()
		for buttonNumb in xrange(groupSize):
			tmpRB = ui.RadioButton()
			tmpRB.SetParent(self)
			tmpRB.SetUpVisual("d:/ymir work/ui/pages/buttons/but_pages_norm.tga")
			tmpRB.SetOverVisual("d:/ymir work/ui/pages/buttons/but_pages_hover.tga")
			tmpRB.SetDownVisual("d:/ymir work/ui/pages/buttons/but_pages_down.tga")
			tmpRB.SetDisableVisual("d:/ymir work/ui/pages/buttons/but_pages_disable.tga")
			tmpRB.SetPosition(__GetButtonX(buttonNumb, tmpRB.GetWidth()), 298)
			tmpRB.Show()
			self.reworkedRadioButtonGroup.AddButton(tmpRB, ui.__mem_func__(self.OnClickTabButton), None)

	def __SetReworkedTabNames(self, groupSize):
		for buttonNumb in xrange(groupSize):
			self.reworkedRadioButtonGroup.SetText(buttonNumb, constInfo.NumberToStrRomanNumerals((buttonNumb + 1)))
			self.reworkedRadioButtonGroup.SetTextPosition(buttonNumb, 1, -1)
			self.reworkedRadioButtonGroup.SetToolTipText(buttonNumb, shop.GetTabName(buttonNumb).replace("_", " "))
	
	#########################################

search this:

		self.smallRadioButtonGroup = ui.RadioButtonGroup.Create([[smallTab1, lambda : self.OnClickTabButton(0), None], [smallTab2, lambda : self.OnClickTabButton(1), None], [smallTab3, lambda : self.OnClickTabButton(2), None]])
		self.middleRadioButtonGroup = ui.RadioButtonGroup.Create([[middleTab1, lambda : self.OnClickTabButton(0), None], [middleTab2, lambda : self.OnClickTabButton(1), None]])

modify to:

		self.smallRadioButtonGroup = ui.RadioButtonGroup.Create([[smallTab1, ui.__mem_func__(self.OnClickTabButton), None], [smallTab2, ui.__mem_func__(self.OnClickTabButton), None], [smallTab3, ui.__mem_func__(self.OnClickTabButton), None]])
		self.middleRadioButtonGroup = ui.RadioButtonGroup.Create([[middleTab1, ui.__mem_func__(self.OnClickTabButton), None], [middleTab2, ui.__mem_func__(self.OnClickTabButton), None]])
		self.reworkedRadioButtonGroup = None

search this:

		if isPrivateShop:
			self.__HideMiddleTabs()
			self.__HideSmallTabs()

replace like this:

		if isPrivateShop:
			self.__HideMiddleTabs()
			self.__HideSmallTabs()
		else:
			tabCount = shop.GetTabCount()
			self.__CreateReworkedShopButtons(tabCount)
			self.__SetReworkedTabNames(tabCount)
			self.reworkedRadioButtonGroup.OnClick(0)