package main

import (
	"fmt"
	"strconv"
	"strings"

	"goatrading/internal/market"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
)

func main() {
	a := app.New()
	w := a.NewWindow("Bitcoin Auto Trader")

	// 가격 표시 레이블
	priceLabel := widget.NewLabel("Current Price:")
	priceValue := widget.NewLabel("0")

	// 조회 버튼
	inquiryButton := widget.NewButton("Inquiry", func() {
		price, err := market.GetCurrentPrice()
		if err != nil {
			priceValue.SetText(fmt.Sprintf("Error: %v", err))
			return
		}

		// 가격을 문자열로 변환하고 천 단위 구분자 추가
		priceStr := strconv.FormatFloat(price, 'f', 0, 64)
		parts := make([]string, 0)
		for i := len(priceStr); i > 0; i -= 3 {
			start := i - 3
			if start < 0 {
				start = 0
			}
			parts = append([]string{priceStr[start:i]}, parts...)
		}
		formattedPrice := strings.Join(parts, ",")

		priceValue.SetText(formattedPrice)
	})

	// 레이아웃 구성
	content := container.NewVBox(
		container.NewHBox(priceLabel, priceValue),
		inquiryButton,
	)

	w.SetContent(content)
	w.Resize(fyne.NewSize(800, 600))
	w.Show()
	a.Run()
}
