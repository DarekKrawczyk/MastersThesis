PULSONIX_LIBRARY_ASCII "SamacSys ECAD Model"
//327580/1279352/2.50/28/3/Integrated Circuit

(asciiHeader
	(fileUnits MM)
)
(library Library_1
	(padStyleDef "r152.6_43.5"
		(holeDiam 0)
		(padShape (layerNumRef 1) (padShapeType Rect)  (shapeWidth 0.435) (shapeHeight 1.526))
		(padShape (layerNumRef 16) (padShapeType Ellipse)  (shapeWidth 0) (shapeHeight 0))
	)
	(textStyleDef "Normal"
		(font
			(fontType Stroke)
			(fontFace "Helvetica")
			(fontHeight 1.27)
			(strokeWidth 0.127)
		)
	)
	(patternDef "SOP64P601X175-28N" (originalName "SOP64P601X175-28N")
		(multiLayer
			(pad (padNum 1) (padStyleRef r152.6_43.5) (pt -2.712, 4.128) (rotation 90))
			(pad (padNum 2) (padStyleRef r152.6_43.5) (pt -2.712, 3.492) (rotation 90))
			(pad (padNum 3) (padStyleRef r152.6_43.5) (pt -2.712, 2.858) (rotation 90))
			(pad (padNum 4) (padStyleRef r152.6_43.5) (pt -2.712, 2.222) (rotation 90))
			(pad (padNum 5) (padStyleRef r152.6_43.5) (pt -2.712, 1.588) (rotation 90))
			(pad (padNum 6) (padStyleRef r152.6_43.5) (pt -2.712, 0.952) (rotation 90))
			(pad (padNum 7) (padStyleRef r152.6_43.5) (pt -2.712, 0.318) (rotation 90))
			(pad (padNum 8) (padStyleRef r152.6_43.5) (pt -2.712, -0.318) (rotation 90))
			(pad (padNum 9) (padStyleRef r152.6_43.5) (pt -2.712, -0.952) (rotation 90))
			(pad (padNum 10) (padStyleRef r152.6_43.5) (pt -2.712, -1.588) (rotation 90))
			(pad (padNum 11) (padStyleRef r152.6_43.5) (pt -2.712, -2.222) (rotation 90))
			(pad (padNum 12) (padStyleRef r152.6_43.5) (pt -2.712, -2.858) (rotation 90))
			(pad (padNum 13) (padStyleRef r152.6_43.5) (pt -2.712, -3.492) (rotation 90))
			(pad (padNum 14) (padStyleRef r152.6_43.5) (pt -2.712, -4.128) (rotation 90))
			(pad (padNum 15) (padStyleRef r152.6_43.5) (pt 2.712, -4.128) (rotation 90))
			(pad (padNum 16) (padStyleRef r152.6_43.5) (pt 2.712, -3.492) (rotation 90))
			(pad (padNum 17) (padStyleRef r152.6_43.5) (pt 2.712, -2.858) (rotation 90))
			(pad (padNum 18) (padStyleRef r152.6_43.5) (pt 2.712, -2.222) (rotation 90))
			(pad (padNum 19) (padStyleRef r152.6_43.5) (pt 2.712, -1.588) (rotation 90))
			(pad (padNum 20) (padStyleRef r152.6_43.5) (pt 2.712, -0.952) (rotation 90))
			(pad (padNum 21) (padStyleRef r152.6_43.5) (pt 2.712, -0.318) (rotation 90))
			(pad (padNum 22) (padStyleRef r152.6_43.5) (pt 2.712, 0.318) (rotation 90))
			(pad (padNum 23) (padStyleRef r152.6_43.5) (pt 2.712, 0.952) (rotation 90))
			(pad (padNum 24) (padStyleRef r152.6_43.5) (pt 2.712, 1.588) (rotation 90))
			(pad (padNum 25) (padStyleRef r152.6_43.5) (pt 2.712, 2.222) (rotation 90))
			(pad (padNum 26) (padStyleRef r152.6_43.5) (pt 2.712, 2.858) (rotation 90))
			(pad (padNum 27) (padStyleRef r152.6_43.5) (pt 2.712, 3.492) (rotation 90))
			(pad (padNum 28) (padStyleRef r152.6_43.5) (pt 2.712, 4.128) (rotation 90))
		)
		(layerContents (layerNumRef 18)
			(attr "RefDes" "RefDes" (pt 0, 0) (textStyleRef "Normal") (isVisible True))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt -3.725 5.241) (pt 3.725 5.241) (width 0.05))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt 3.725 5.241) (pt 3.725 -5.241) (width 0.05))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt 3.725 -5.241) (pt -3.725 -5.241) (width 0.05))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt -3.725 -5.241) (pt -3.725 5.241) (width 0.05))
		)
		(layerContents (layerNumRef 28)
			(line (pt -1.95 4.946) (pt 1.95 4.946) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt 1.95 4.946) (pt 1.95 -4.946) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt 1.95 -4.946) (pt -1.95 -4.946) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt -1.95 -4.946) (pt -1.95 4.946) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt -1.95 4.312) (pt -1.314 4.946) (width 0.025))
		)
		(layerContents (layerNumRef 18)
			(line (pt -1.6 4.946) (pt 1.6 4.946) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt 1.6 4.946) (pt 1.6 -4.946) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt 1.6 -4.946) (pt -1.6 -4.946) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt -1.6 -4.946) (pt -1.6 4.946) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt -3.475 4.695) (pt -1.95 4.695) (width 0.2))
		)
	)
	(symbolDef "LTC2439-1IGN#PBF" (originalName "LTC2439-1IGN#PBF")

		(pin (pinNum 1) (pt 0 mils 0 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -25 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 2) (pt 0 mils -100 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -125 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 3) (pt 0 mils -200 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -225 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 4) (pt 0 mils -300 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -325 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 5) (pt 0 mils -400 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -425 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 6) (pt 0 mils -500 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -525 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 7) (pt 0 mils -600 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -625 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 8) (pt 0 mils -700 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -725 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 9) (pt 0 mils -800 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -825 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 10) (pt 0 mils -900 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -925 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 11) (pt 0 mils -1000 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -1025 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 12) (pt 0 mils -1100 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -1125 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 13) (pt 0 mils -1200 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -1225 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 14) (pt 0 mils -1300 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -1325 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 15) (pt 1200 mils 0 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 970 mils -25 mils) (rotation 0]) (justify "Right") (textStyleRef "Normal"))
		))
		(pin (pinNum 16) (pt 1200 mils -100 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 970 mils -125 mils) (rotation 0]) (justify "Right") (textStyleRef "Normal"))
		))
		(pin (pinNum 17) (pt 1200 mils -200 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 970 mils -225 mils) (rotation 0]) (justify "Right") (textStyleRef "Normal"))
		))
		(pin (pinNum 18) (pt 1200 mils -300 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 970 mils -325 mils) (rotation 0]) (justify "Right") (textStyleRef "Normal"))
		))
		(pin (pinNum 19) (pt 1200 mils -400 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 970 mils -425 mils) (rotation 0]) (justify "Right") (textStyleRef "Normal"))
		))
		(pin (pinNum 20) (pt 1200 mils -500 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 970 mils -525 mils) (rotation 0]) (justify "Right") (textStyleRef "Normal"))
		))
		(pin (pinNum 21) (pt 1200 mils -600 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 970 mils -625 mils) (rotation 0]) (justify "Right") (textStyleRef "Normal"))
		))
		(pin (pinNum 22) (pt 1200 mils -700 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 970 mils -725 mils) (rotation 0]) (justify "Right") (textStyleRef "Normal"))
		))
		(pin (pinNum 23) (pt 1200 mils -800 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 970 mils -825 mils) (rotation 0]) (justify "Right") (textStyleRef "Normal"))
		))
		(pin (pinNum 24) (pt 1200 mils -900 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 970 mils -925 mils) (rotation 0]) (justify "Right") (textStyleRef "Normal"))
		))
		(pin (pinNum 25) (pt 1200 mils -1000 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 970 mils -1025 mils) (rotation 0]) (justify "Right") (textStyleRef "Normal"))
		))
		(pin (pinNum 26) (pt 1200 mils -1100 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 970 mils -1125 mils) (rotation 0]) (justify "Right") (textStyleRef "Normal"))
		))
		(pin (pinNum 27) (pt 1200 mils -1200 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 970 mils -1225 mils) (rotation 0]) (justify "Right") (textStyleRef "Normal"))
		))
		(pin (pinNum 28) (pt 1200 mils -1300 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 970 mils -1325 mils) (rotation 0]) (justify "Right") (textStyleRef "Normal"))
		))
		(line (pt 200 mils 100 mils) (pt 1000 mils 100 mils) (width 6 mils))
		(line (pt 1000 mils 100 mils) (pt 1000 mils -1400 mils) (width 6 mils))
		(line (pt 1000 mils -1400 mils) (pt 200 mils -1400 mils) (width 6 mils))
		(line (pt 200 mils -1400 mils) (pt 200 mils 100 mils) (width 6 mils))
		(attr "RefDes" "RefDes" (pt 1050 mils 300 mils) (justify Left) (isVisible True) (textStyleRef "Normal"))
		(attr "Type" "Type" (pt 1050 mils 200 mils) (justify Left) (isVisible True) (textStyleRef "Normal"))

	)
	(compDef "LTC2439-1IGN#PBF" (originalName "LTC2439-1IGN#PBF") (compHeader (numPins 28) (numParts 1) (refDesPrefix IC)
		)
		(compPin "1" (pinName "CH8") (partNum 1) (symPinNum 1) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "2" (pinName "CH9") (partNum 1) (symPinNum 2) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "3" (pinName "CH10") (partNum 1) (symPinNum 3) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "4" (pinName "CH11") (partNum 1) (symPinNum 4) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "5" (pinName "CH12") (partNum 1) (symPinNum 5) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "6" (pinName "CH13") (partNum 1) (symPinNum 6) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "7" (pinName "CH14") (partNum 1) (symPinNum 7) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "8" (pinName "CH15") (partNum 1) (symPinNum 8) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "9" (pinName "VCC") (partNum 1) (symPinNum 9) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "10" (pinName "COM") (partNum 1) (symPinNum 10) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "11" (pinName "REF+") (partNum 1) (symPinNum 11) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "12" (pinName "REF–") (partNum 1) (symPinNum 12) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "13" (pinName "NC_1") (partNum 1) (symPinNum 13) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "14" (pinName "NC_2") (partNum 1) (symPinNum 14) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "28" (pinName "CH7") (partNum 1) (symPinNum 15) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "27" (pinName "CH6") (partNum 1) (symPinNum 16) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "26" (pinName "CH5") (partNum 1) (symPinNum 17) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "25" (pinName "CH4") (partNum 1) (symPinNum 18) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "24" (pinName "CH3") (partNum 1) (symPinNum 19) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "23" (pinName "CH2") (partNum 1) (symPinNum 20) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "22" (pinName "CH1") (partNum 1) (symPinNum 21) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "21" (pinName "CH0") (partNum 1) (symPinNum 22) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "20" (pinName "SDI") (partNum 1) (symPinNum 23) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "19" (pinName "FO") (partNum 1) (symPinNum 24) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "18" (pinName "SCK") (partNum 1) (symPinNum 25) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "17" (pinName "SDO") (partNum 1) (symPinNum 26) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "16" (pinName "__CS") (partNum 1) (symPinNum 27) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "15" (pinName "GND") (partNum 1) (symPinNum 28) (gateEq 0) (pinEq 0) (pinType Unknown))
		(attachedSymbol (partNum 1) (altType Normal) (symbolName "LTC2439-1IGN#PBF"))
		(attachedPattern (patternNum 1) (patternName "SOP64P601X175-28N")
			(numPads 28)
			(padPinMap
				(padNum 1) (compPinRef "1")
				(padNum 2) (compPinRef "2")
				(padNum 3) (compPinRef "3")
				(padNum 4) (compPinRef "4")
				(padNum 5) (compPinRef "5")
				(padNum 6) (compPinRef "6")
				(padNum 7) (compPinRef "7")
				(padNum 8) (compPinRef "8")
				(padNum 9) (compPinRef "9")
				(padNum 10) (compPinRef "10")
				(padNum 11) (compPinRef "11")
				(padNum 12) (compPinRef "12")
				(padNum 13) (compPinRef "13")
				(padNum 14) (compPinRef "14")
				(padNum 15) (compPinRef "15")
				(padNum 16) (compPinRef "16")
				(padNum 17) (compPinRef "17")
				(padNum 18) (compPinRef "18")
				(padNum 19) (compPinRef "19")
				(padNum 20) (compPinRef "20")
				(padNum 21) (compPinRef "21")
				(padNum 22) (compPinRef "22")
				(padNum 23) (compPinRef "23")
				(padNum 24) (compPinRef "24")
				(padNum 25) (compPinRef "25")
				(padNum 26) (compPinRef "26")
				(padNum 27) (compPinRef "27")
				(padNum 28) (compPinRef "28")
			)
		)
		(attr "Manufacturer_Name" "Analog Devices")
		(attr "Manufacturer_Part_Number" "LTC2439-1IGN#PBF")
		(attr "Mouser Part Number" "584-LTC2439-1IGN#PBF")
		(attr "Mouser Price/Stock" "https://www.mouser.co.uk/ProductDetail/Analog-Devices/LTC2439-1IGNPBF?qs=hVkxg5c3xu%2F3ZSVw0cv92Q%3D%3D")
		(attr "Arrow Part Number" "LTC2439-1IGN#PBF")
		(attr "Arrow Price/Stock" "https://www.arrow.com/en/products/ltc2439-1ignpbf/analog-devices?region=nac")
		(attr "Description" "LINEAR TECHNOLOGY - LTC2439-1IGN#PBF - Analogue to Digital Converter, Octal, 16 bit, 6.9 SPS, Differential, Single Ended, SPI, Single")
		(attr "<Hyperlink>" "https://datasheet.datasheetarchive.com/originals/distributors/SFDatasheet-4/sf-00091692.pdf")
		(attr "<Component Height>" "1.75")
		(attr "<STEP Filename>" "LTC2439-1IGN#PBF.stp")
		(attr "<STEP Offsets>" "X=0;Y=0;Z=0")
		(attr "<STEP Rotation>" "X=0;Y=0;Z=0")
	)

)
