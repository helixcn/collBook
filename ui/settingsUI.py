# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/settingsUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settingsWindow(object):
    def setupUi(self, settingsWindow):
        settingsWindow.setObjectName("settingsWindow")
        settingsWindow.resize(780, 645)
        settingsWindow.setMinimumSize(QtCore.QSize(0, 0))
        settingsWindow.setStyleSheet("font: 12pt \"Cantarell\";")
        self.centralwidget = QtWidgets.QWidget(settingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.upperHorizontalLayout = QtWidgets.QHBoxLayout()
        self.upperHorizontalLayout.setObjectName("upperHorizontalLayout")
        self.page_Display = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_Display.sizePolicy().hasHeightForWidth())
        self.page_Display.setSizePolicy(sizePolicy)
        self.page_Display.setLineWidth(1)
        self.page_Display.setObjectName("page_Display")
        item = QtWidgets.QListWidgetItem()
        self.page_Display.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.page_Display.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.page_Display.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setItalic(False)
        item.setFont(font)
        self.page_Display.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.page_Display.addItem(item)
        self.upperHorizontalLayout.addWidget(self.page_Display)
        self.settingsPage = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.settingsPage.sizePolicy().hasHeightForWidth())
        self.settingsPage.setSizePolicy(sizePolicy)
        self.settingsPage.setObjectName("settingsPage")
        self.associatedTaxaPage = QtWidgets.QWidget()
        self.associatedTaxaPage.setObjectName("associatedTaxaPage")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.associatedTaxaPage)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox_3 = QtWidgets.QGroupBox(self.associatedTaxaPage)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.value_associatedAlways = QtWidgets.QRadioButton(self.groupBox_3)
        self.value_associatedAlways.setChecked(True)
        self.value_associatedAlways.setObjectName("value_associatedAlways")
        self.verticalLayout_2.addWidget(self.value_associatedAlways)
        self.value_associatedOnly = QtWidgets.QRadioButton(self.groupBox_3)
        self.value_associatedOnly.setObjectName("value_associatedOnly")
        self.verticalLayout_2.addWidget(self.value_associatedOnly)
        self.value_associatedNever = QtWidgets.QRadioButton(self.groupBox_3)
        self.value_associatedNever.setObjectName("value_associatedNever")
        self.verticalLayout_2.addWidget(self.value_associatedNever)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout_9.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.settingsPage.addWidget(self.associatedTaxaPage)
        self.catalogNumberPage = QtWidgets.QWidget()
        self.catalogNumberPage.setObjectName("catalogNumberPage")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.catalogNumberPage)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.value_assignCatalogNumbers = QtWidgets.QGroupBox(self.catalogNumberPage)
        self.value_assignCatalogNumbers.setCheckable(True)
        self.value_assignCatalogNumbers.setObjectName("value_assignCatalogNumbers")
        self.formLayout = QtWidgets.QFormLayout(self.value_assignCatalogNumbers)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.value_inc_Barcode = QtWidgets.QCheckBox(self.value_assignCatalogNumbers)
        self.value_inc_Barcode.setObjectName("value_inc_Barcode")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.value_inc_Barcode)
        self.label_6 = QtWidgets.QLabel(self.value_assignCatalogNumbers)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.value_catalogNumberPrefix = QtWidgets.QLineEdit(self.value_assignCatalogNumbers)
        self.value_catalogNumberPrefix.setAlignment(QtCore.Qt.AlignCenter)
        self.value_catalogNumberPrefix.setObjectName("value_catalogNumberPrefix")
        self.horizontalLayout_4.addWidget(self.value_catalogNumberPrefix)
        self.label_7 = QtWidgets.QLabel(self.value_assignCatalogNumbers)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.value_catalogNumberDigits = QtWidgets.QSpinBox(self.value_assignCatalogNumbers)
        self.value_catalogNumberDigits.setAlignment(QtCore.Qt.AlignCenter)
        self.value_catalogNumberDigits.setMinimum(1)
        self.value_catalogNumberDigits.setMaximum(10)
        self.value_catalogNumberDigits.setObjectName("value_catalogNumberDigits")
        self.horizontalLayout_4.addWidget(self.value_catalogNumberDigits)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_8 = QtWidgets.QLabel(self.value_assignCatalogNumbers)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.value_catalogNumberStartingNum = QtWidgets.QSpinBox(self.value_assignCatalogNumbers)
        self.value_catalogNumberStartingNum.setAlignment(QtCore.Qt.AlignCenter)
        self.value_catalogNumberStartingNum.setMaximum(999999999)
        self.value_catalogNumberStartingNum.setObjectName("value_catalogNumberStartingNum")
        self.horizontalLayout_5.addWidget(self.value_catalogNumberStartingNum)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.label_10 = QtWidgets.QLabel(self.value_assignCatalogNumbers)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_catalogNumber_Preview = QtWidgets.QLabel(self.value_assignCatalogNumbers)
        self.label_catalogNumber_Preview.setText("")
        self.label_catalogNumber_Preview.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_catalogNumber_Preview.setObjectName("label_catalogNumber_Preview")
        self.horizontalLayout_6.addWidget(self.label_catalogNumber_Preview)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(10, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.gridLayout_6.addWidget(self.value_assignCatalogNumbers, 0, 0, 1, 1)
        self.settingsPage.addWidget(self.catalogNumberPage)
        self.themePage = QtWidgets.QWidget()
        self.themePage.setObjectName("themePage")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.themePage)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem4, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.themePage)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.value_LightTheme = QtWidgets.QRadioButton(self.groupBox_2)
        self.value_LightTheme.setObjectName("value_LightTheme")
        self.gridLayout_8.addWidget(self.value_LightTheme, 2, 0, 1, 1)
        self.value_DarkTheme = QtWidgets.QRadioButton(self.groupBox_2)
        self.value_DarkTheme.setObjectName("value_DarkTheme")
        self.gridLayout_8.addWidget(self.value_DarkTheme, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_8.addWidget(self.label_11, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_7.addWidget(self.groupBox_2, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem5, 0, 1, 1, 1)
        self.settingsPage.addWidget(self.themePage)
        self.labelPrefPage = QtWidgets.QWidget()
        self.labelPrefPage.setObjectName("labelPrefPage")
        self.gridLayout = QtWidgets.QGridLayout(self.labelPrefPage)
        self.gridLayout.setObjectName("gridLayout")
        self.labelDimentionsGroup = QtWidgets.QGroupBox(self.labelPrefPage)
        self.labelDimentionsGroup.setObjectName("labelDimentionsGroup")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.labelDimentionsGroup)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.xLabel = QtWidgets.QLabel(self.labelDimentionsGroup)
        self.xLabel.setObjectName("xLabel")
        self.gridLayout_5.addWidget(self.xLabel, 0, 0, 1, 1)
        self.yLabel = QtWidgets.QLabel(self.labelDimentionsGroup)
        self.yLabel.setObjectName("yLabel")
        self.gridLayout_5.addWidget(self.yLabel, 0, 2, 1, 1)
        self.value_X = QtWidgets.QSpinBox(self.labelDimentionsGroup)
        self.value_X.setMinimum(1)
        self.value_X.setMaximum(9999)
        self.value_X.setObjectName("value_X")
        self.gridLayout_5.addWidget(self.value_X, 1, 0, 1, 1)
        self.value_Y = QtWidgets.QSpinBox(self.labelDimentionsGroup)
        self.value_Y.setMinimum(1)
        self.value_Y.setMaximum(9999)
        self.value_Y.setObjectName("value_Y")
        self.gridLayout_5.addWidget(self.value_Y, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.labelDimentionsGroup, 0, 1, 1, 1)
        self.labelFontGroup = QtWidgets.QGroupBox(self.labelPrefPage)
        self.labelFontGroup.setObjectName("labelFontGroup")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.labelFontGroup)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.value_RelFont = QtWidgets.QSpinBox(self.labelFontGroup)
        self.value_RelFont.setProperty("value", 12)
        self.value_RelFont.setObjectName("value_RelFont")
        self.gridLayout_10.addWidget(self.value_RelFont, 1, 1, 1, 1)
        self.fontNameLabel = QtWidgets.QLabel(self.labelFontGroup)
        self.fontNameLabel.setObjectName("fontNameLabel")
        self.gridLayout_10.addWidget(self.fontNameLabel, 0, 0, 1, 1)
        self.relFontLabel = QtWidgets.QLabel(self.labelFontGroup)
        self.relFontLabel.setObjectName("relFontLabel")
        self.gridLayout_10.addWidget(self.relFontLabel, 1, 0, 1, 1)
        self.value_fontName = QtWidgets.QComboBox(self.labelFontGroup)
        self.value_fontName.setObjectName("value_fontName")
        self.value_fontName.addItem("")
        self.value_fontName.addItem("")
        self.value_fontName.addItem("")
        self.gridLayout_10.addWidget(self.value_fontName, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.labelFontGroup, 0, 0, 1, 1)
        self.labelIncludeGroup = QtWidgets.QGroupBox(self.labelPrefPage)
        self.labelIncludeGroup.setObjectName("labelIncludeGroup")
        self.formLayout_3 = QtWidgets.QFormLayout(self.labelIncludeGroup)
        self.formLayout_3.setObjectName("formLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.value_inc_Associated = QtWidgets.QCheckBox(self.labelIncludeGroup)
        self.value_inc_Associated.setChecked(True)
        self.value_inc_Associated.setObjectName("value_inc_Associated")
        self.horizontalLayout_7.addWidget(self.value_inc_Associated)
        self.label_9 = QtWidgets.QLabel(self.labelIncludeGroup)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.value_max_Associated = QtWidgets.QSpinBox(self.labelIncludeGroup)
        self.value_max_Associated.setMinimum(1)
        self.value_max_Associated.setProperty("value", 10)
        self.value_max_Associated.setObjectName("value_max_Associated")
        self.horizontalLayout_7.addWidget(self.value_max_Associated)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 2)
        self.horizontalLayout_7.setStretch(2, 1)
        self.horizontalLayout_7.setStretch(3, 1)
        self.formLayout_3.setLayout(2, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_7)
        self.value_inc_VerifiedBy = QtWidgets.QCheckBox(self.labelIncludeGroup)
        self.value_inc_VerifiedBy.setObjectName("value_inc_VerifiedBy")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.value_inc_VerifiedBy)
        self.value_VerifiedBy = QtWidgets.QLineEdit(self.labelIncludeGroup)
        self.value_VerifiedBy.setObjectName("value_VerifiedBy")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.value_VerifiedBy)
        self.value_inc_CollectionName = QtWidgets.QCheckBox(self.labelIncludeGroup)
        self.value_inc_CollectionName.setObjectName("value_inc_CollectionName")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.value_inc_CollectionName)
        self.value_CollectionName = QtWidgets.QPlainTextEdit(self.labelIncludeGroup)
        self.value_CollectionName.setEnabled(False)
        self.value_CollectionName.setObjectName("value_CollectionName")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.value_CollectionName)
        self.value_inc_Logo = QtWidgets.QGroupBox(self.labelIncludeGroup)
        self.value_inc_Logo.setCheckable(True)
        self.value_inc_Logo.setChecked(False)
        self.value_inc_Logo.setObjectName("value_inc_Logo")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.value_inc_Logo)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.value_inc_Logo)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.value_LogoAlignment = QtWidgets.QComboBox(self.value_inc_Logo)
        self.value_LogoAlignment.setObjectName("value_LogoAlignment")
        self.value_LogoAlignment.addItem("")
        self.value_LogoAlignment.addItem("")
        self.value_LogoAlignment.addItem("")
        self.value_LogoAlignment.addItem("")
        self.value_LogoAlignment.addItem("")
        self.value_LogoAlignment.addItem("")
        self.value_LogoAlignment.addItem("")
        self.value_LogoAlignment.addItem("")
        self.value_LogoAlignment.addItem("")
        self.horizontalLayout.addWidget(self.value_LogoAlignment)
        self.label_5 = QtWidgets.QLabel(self.value_inc_Logo)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.value_LogoMargin = QtWidgets.QSpinBox(self.value_inc_Logo)
        self.value_LogoMargin.setMaximum(9999)
        self.value_LogoMargin.setProperty("value", 3)
        self.value_LogoMargin.setObjectName("value_LogoMargin")
        self.horizontalLayout.addWidget(self.value_LogoMargin)
        self.horizontalLayout.setStretch(1, 10)
        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.value_LogoPath = QtWidgets.QLineEdit(self.value_inc_Logo)
        self.value_LogoPath.setEnabled(False)
        self.value_LogoPath.setObjectName("value_LogoPath")
        self.gridLayout_4.addWidget(self.value_LogoPath, 0, 1, 1, 1)
        self.toolButton_GetLogoPath = QtWidgets.QToolButton(self.value_inc_Logo)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rc_/chevron-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_GetLogoPath.setIcon(icon)
        self.toolButton_GetLogoPath.setIconSize(QtCore.QSize(18, 18))
        self.toolButton_GetLogoPath.setObjectName("toolButton_GetLogoPath")
        self.gridLayout_4.addWidget(self.toolButton_GetLogoPath, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.value_inc_Logo)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.value_LogoScaling = QtWidgets.QSlider(self.value_inc_Logo)
        self.value_LogoScaling.setMaximum(100)
        self.value_LogoScaling.setProperty("value", 100)
        self.value_LogoScaling.setOrientation(QtCore.Qt.Horizontal)
        self.value_LogoScaling.setObjectName("value_LogoScaling")
        self.horizontalLayout_2.addWidget(self.value_LogoScaling)
        self.label_scalingValue = QtWidgets.QLabel(self.value_inc_Logo)
        self.label_scalingValue.setText("")
        self.label_scalingValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_scalingValue.setObjectName("label_scalingValue")
        self.horizontalLayout_2.addWidget(self.label_scalingValue)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 8)
        self.horizontalLayout_2.setStretch(2, 2)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.value_inc_Logo)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.value_LogoOpacity = QtWidgets.QSlider(self.value_inc_Logo)
        self.value_LogoOpacity.setMaximum(100)
        self.value_LogoOpacity.setProperty("value", 30)
        self.value_LogoOpacity.setOrientation(QtCore.Qt.Horizontal)
        self.value_LogoOpacity.setObjectName("value_LogoOpacity")
        self.horizontalLayout_3.addWidget(self.value_LogoOpacity)
        self.label_opacityValue = QtWidgets.QLabel(self.value_inc_Logo)
        self.label_opacityValue.setText("")
        self.label_opacityValue.setObjectName("label_opacityValue")
        self.horizontalLayout_3.addWidget(self.label_opacityValue)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 8)
        self.horizontalLayout_3.setStretch(2, 2)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 3, 0, 1, 2)
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.value_inc_Logo)
        self.gridLayout.addWidget(self.labelIncludeGroup, 1, 0, 1, 2)
        self.settingsPage.addWidget(self.labelPrefPage)
        self.TaxPrefPage = QtWidgets.QWidget()
        self.TaxPrefPage.setObjectName("TaxPrefPage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.TaxPrefPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupbox_Kingdom = QtWidgets.QGroupBox(self.TaxPrefPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupbox_Kingdom.sizePolicy().hasHeightForWidth())
        self.groupbox_Kingdom.setSizePolicy(sizePolicy)
        self.groupbox_Kingdom.setObjectName("groupbox_Kingdom")
        self.formLayout_6 = QtWidgets.QFormLayout(self.groupbox_Kingdom)
        self.formLayout_6.setObjectName("formLayout_6")
        self.value_Kingdom = QtWidgets.QComboBox(self.groupbox_Kingdom)
        self.value_Kingdom.setObjectName("value_Kingdom")
        self.value_Kingdom.addItem("")
        self.value_Kingdom.addItem("")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.value_Kingdom)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_6.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem7)
        self.gridLayout_3.addWidget(self.groupbox_Kingdom, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.TaxPrefPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_5 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_TaxAlignSource = QtWidgets.QLabel(self.groupBox)
        self.label_TaxAlignSource.setObjectName("label_TaxAlignSource")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_TaxAlignSource)
        self.value_TaxAlignSource = QtWidgets.QComboBox(self.groupBox)
        self.value_TaxAlignSource.setObjectName("value_TaxAlignSource")
        self.value_TaxAlignSource.addItem("")
        self.value_TaxAlignSource.addItem("")
        self.value_TaxAlignSource.addItem("")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.value_TaxAlignSource)
        self.label_NameChangePolicy = QtWidgets.QLabel(self.groupBox)
        self.label_NameChangePolicy.setObjectName("label_NameChangePolicy")
        self.formLayout_5.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_NameChangePolicy)
        self.value_NameChangePolicy = QtWidgets.QComboBox(self.groupBox)
        self.value_NameChangePolicy.setObjectName("value_NameChangePolicy")
        self.value_NameChangePolicy.addItem("")
        self.value_NameChangePolicy.addItem("")
        self.formLayout_5.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.value_NameChangePolicy)
        self.label_AuthChangePolicy = QtWidgets.QLabel(self.groupBox)
        self.label_AuthChangePolicy.setObjectName("label_AuthChangePolicy")
        self.formLayout_5.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_AuthChangePolicy)
        self.value_AuthChangePolicy = QtWidgets.QComboBox(self.groupBox)
        self.value_AuthChangePolicy.setObjectName("value_AuthChangePolicy")
        self.value_AuthChangePolicy.addItem("")
        self.value_AuthChangePolicy.addItem("")
        self.value_AuthChangePolicy.addItem("")
        self.formLayout_5.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.value_AuthChangePolicy)
        self.groupbox_TNRS = QtWidgets.QGroupBox(self.groupBox)
        self.groupbox_TNRS.setEnabled(False)
        self.groupbox_TNRS.setObjectName("groupbox_TNRS")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupbox_TNRS)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.groupbox_TNRS)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.value_TNRS_Threshold = QtWidgets.QSpinBox(self.groupbox_TNRS)
        self.value_TNRS_Threshold.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.value_TNRS_Threshold.setMinimum(1)
        self.value_TNRS_Threshold.setMaximum(100)
        self.value_TNRS_Threshold.setProperty("value", 1)
        self.value_TNRS_Threshold.setObjectName("value_TNRS_Threshold")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.value_TNRS_Threshold)
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.groupbox_TNRS)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)
        self.settingsPage.addWidget(self.TaxPrefPage)
        self.upperHorizontalLayout.addWidget(self.settingsPage)
        self.upperHorizontalLayout.setStretch(1, 4)
        self.verticalLayout.addLayout(self.upperHorizontalLayout)
        self.lowerHorizontalLayout = QtWidgets.QHBoxLayout()
        self.lowerHorizontalLayout.setObjectName("lowerHorizontalLayout")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lowerHorizontalLayout.addItem(spacerItem8)
        self.button_Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.button_Cancel.setObjectName("button_Cancel")
        self.lowerHorizontalLayout.addWidget(self.button_Cancel)
        self.button_SaveExit = QtWidgets.QPushButton(self.centralwidget)
        self.button_SaveExit.setAutoDefault(False)
        self.button_SaveExit.setObjectName("button_SaveExit")
        self.lowerHorizontalLayout.addWidget(self.button_SaveExit)
        self.verticalLayout.addLayout(self.lowerHorizontalLayout)
        self.verticalLayout.setStretch(1, 3)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        settingsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(settingsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 26))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        settingsWindow.setMenuBar(self.menubar)

        self.retranslateUi(settingsWindow)
        self.settingsPage.setCurrentIndex(3)
        self.value_fontName.setCurrentIndex(1)
        self.value_LogoAlignment.setCurrentIndex(4)
        self.value_Kingdom.setCurrentIndex(1)
        self.value_inc_VerifiedBy.toggled['bool'].connect(self.value_VerifiedBy.setEnabled)
        self.value_inc_VerifiedBy.stateChanged['int'].connect(self.value_VerifiedBy.setFocus)
        self.value_inc_CollectionName.toggled['bool'].connect(self.value_CollectionName.setEnabled)
        self.value_inc_CollectionName.stateChanged['int'].connect(self.value_CollectionName.setFocus)
        self.value_TaxAlignSource.currentTextChanged['QString'].connect(settingsWindow.toggleTNRSSettings)
        self.page_Display.currentRowChanged['int'].connect(self.settingsPage.setCurrentIndex)
        self.value_Kingdom.currentTextChanged['QString'].connect(settingsWindow.kingdomChanged)
        self.value_LogoScaling.sliderMoved['int'].connect(settingsWindow.scalingChanged)
        self.value_LogoOpacity.valueChanged['int'].connect(settingsWindow.opacityChanged)
        self.value_catalogNumberPrefix.textChanged['QString'].connect(settingsWindow.updateCatalogNumberPreview)
        self.value_catalogNumberDigits.valueChanged['QString'].connect(settingsWindow.updateCatalogNumberPreview)
        self.value_catalogNumberStartingNum.valueChanged['QString'].connect(settingsWindow.updateCatalogNumberPreview)
        self.value_catalogNumberDigits.valueChanged['int'].connect(settingsWindow.updateStartingCatalogNumber)
        self.value_assignCatalogNumbers.toggled['bool'].connect(self.value_inc_Barcode.setChecked)
        self.value_inc_Associated.toggled['bool'].connect(self.label_9.setEnabled)
        self.value_inc_Associated.toggled['bool'].connect(self.value_max_Associated.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(settingsWindow)

    def retranslateUi(self, settingsWindow):
        _translate = QtCore.QCoreApplication.translate
        settingsWindow.setWindowTitle(_translate("settingsWindow", "Preferences"))
        __sortingEnabled = self.page_Display.isSortingEnabled()
        self.page_Display.setSortingEnabled(False)
        item = self.page_Display.item(0)
        item.setText(_translate("settingsWindow", "Associated Taxa"))
        item = self.page_Display.item(1)
        item.setText(_translate("settingsWindow", "Catalog Numbers"))
        item = self.page_Display.item(2)
        item.setText(_translate("settingsWindow", "Display (UI)"))
        item = self.page_Display.item(3)
        item.setText(_translate("settingsWindow", "Labels"))
        item = self.page_Display.item(4)
        item.setText(_translate("settingsWindow", "Taxonomy"))
        self.page_Display.setSortingEnabled(__sortingEnabled)
        self.groupBox_3.setTitle(_translate("settingsWindow", "Display associated taxa dialog while refining records:"))
        self.value_associatedAlways.setText(_translate("settingsWindow", "Always"))
        self.value_associatedOnly.setText(_translate("settingsWindow", "Only for sites with more than  1 specimen"))
        self.value_associatedNever.setText(_translate("settingsWindow", "Never"))
        self.value_assignCatalogNumbers.setTitle(_translate("settingsWindow", "Assign Catalog Numbers"))
        self.value_inc_Barcode.setText(_translate("settingsWindow", "Include dummy barcode in label previews"))
        self.label_6.setText(_translate("settingsWindow", "Catalog Number Prefix"))
        self.label_7.setText(_translate("settingsWindow", "Digits"))
        self.label_8.setText(_translate("settingsWindow", "Starting Number"))
        self.label_10.setText(_translate("settingsWindow", "Preview"))
        self.groupBox_2.setTitle(_translate("settingsWindow", "Themes"))
        self.value_LightTheme.setText(_translate("settingsWindow", "Light Theme"))
        self.value_DarkTheme.setText(_translate("settingsWindow", "Dark Theme"))
        self.label_11.setText(_translate("settingsWindow", "Changes applied on next start up."))
        self.labelDimentionsGroup.setTitle(_translate("settingsWindow", "Label dimensions"))
        self.xLabel.setText(_translate("settingsWindow", "width (mm)"))
        self.yLabel.setText(_translate("settingsWindow", "height (mm)"))
        self.labelFontGroup.setTitle(_translate("settingsWindow", "Label Font"))
        self.fontNameLabel.setText(_translate("settingsWindow", "Font"))
        self.relFontLabel.setText(_translate("settingsWindow", "Base font size"))
        self.value_fontName.setItemText(0, _translate("settingsWindow", "Courier"))
        self.value_fontName.setItemText(1, _translate("settingsWindow", "Helvetica"))
        self.value_fontName.setItemText(2, _translate("settingsWindow", "Times"))
        self.labelIncludeGroup.setTitle(_translate("settingsWindow", "Include on label"))
        self.value_inc_Associated.setText(_translate("settingsWindow", "Include associated taxa"))
        self.label_9.setText(_translate("settingsWindow", "Max Taxa:"))
        self.value_inc_VerifiedBy.setText(_translate("settingsWindow", "Include verified by"))
        self.value_inc_CollectionName.setText(_translate("settingsWindow", "Include collection name"))
        self.value_inc_Logo.setTitle(_translate("settingsWindow", "Include collection logo"))
        self.label_2.setText(_translate("settingsWindow", "Alignment"))
        self.value_LogoAlignment.setItemText(0, _translate("settingsWindow", "Upper Left"))
        self.value_LogoAlignment.setItemText(1, _translate("settingsWindow", "Upper Center"))
        self.value_LogoAlignment.setItemText(2, _translate("settingsWindow", "Upper Right"))
        self.value_LogoAlignment.setItemText(3, _translate("settingsWindow", "Center Left"))
        self.value_LogoAlignment.setItemText(4, _translate("settingsWindow", "Centered"))
        self.value_LogoAlignment.setItemText(5, _translate("settingsWindow", "Center Right"))
        self.value_LogoAlignment.setItemText(6, _translate("settingsWindow", "Lower Left"))
        self.value_LogoAlignment.setItemText(7, _translate("settingsWindow", "Lower Center"))
        self.value_LogoAlignment.setItemText(8, _translate("settingsWindow", "Lower Right"))
        self.label_5.setText(_translate("settingsWindow", "Margin (px) "))
        self.toolButton_GetLogoPath.setText(_translate("settingsWindow", "..."))
        self.label_3.setText(_translate("settingsWindow", "Scaling   "))
        self.label_4.setText(_translate("settingsWindow", "Opacity  "))
        self.groupbox_Kingdom.setTitle(_translate("settingsWindow", "Kingdom"))
        self.value_Kingdom.setItemText(0, _translate("settingsWindow", "Fungi"))
        self.value_Kingdom.setItemText(1, _translate("settingsWindow", "Plantae"))
        self.groupBox.setTitle(_translate("settingsWindow", "Taxanomic alignment"))
        self.label_TaxAlignSource.setText(_translate("settingsWindow", "Source"))
        self.value_TaxAlignSource.setItemText(0, _translate("settingsWindow", "ITIS (local)"))
        self.value_TaxAlignSource.setItemText(1, _translate("settingsWindow", "Catalog of Life (web API)"))
        self.value_TaxAlignSource.setItemText(2, _translate("settingsWindow", "Taxonomic Name Resolution Service (web API)"))
        self.label_NameChangePolicy.setText(_translate("settingsWindow", "Name change policy"))
        self.value_NameChangePolicy.setItemText(0, _translate("settingsWindow", "Accept all suggestions"))
        self.value_NameChangePolicy.setItemText(1, _translate("settingsWindow", "Always ask"))
        self.label_AuthChangePolicy.setText(_translate("settingsWindow", "Authority change policy"))
        self.value_AuthChangePolicy.setItemText(0, _translate("settingsWindow", "Accept all suggestions"))
        self.value_AuthChangePolicy.setItemText(1, _translate("settingsWindow", "Always ask"))
        self.value_AuthChangePolicy.setItemText(2, _translate("settingsWindow", "Fill blanks"))
        self.groupbox_TNRS.setTitle(_translate("settingsWindow", "TNRS Settings"))
        self.label.setText(_translate("settingsWindow", "scoreThreshold"))
        self.button_Cancel.setText(_translate("settingsWindow", "Cancel"))
        self.button_SaveExit.setText(_translate("settingsWindow", "Save and exit"))


import Resources_rc
