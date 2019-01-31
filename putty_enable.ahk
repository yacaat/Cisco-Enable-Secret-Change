CoordMode Pixel
counter = 0
Loop{
ImageSearch, FoundX, FoundY, 0, 0, %A_ScreenWidth%, %A_ScreenHeight%, C:\Users\yalina\PycharmProjects\console\putty.png 
    if ErrorLevel = 0
    {
        Break
    }
    if counter > 100
    {
        ExitApp
    }
counter++
;MsgBox, %counter%
}
Send, en{Enter}
Sleep, 500
Send, %1%{Enter}
