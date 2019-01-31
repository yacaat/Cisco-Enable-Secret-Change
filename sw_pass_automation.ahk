MyVar = %1%
Send, en{Enter}
Sleep, 1000
Send, brcd1920{Enter}
Sleep, 1000
Send, sh mac add | i{Space}
;MsgBox, 0,, mmm%MyVar%mmmmm
;MsgBox, 0,, %1% %0%
If (MyVar = "1") {
    WinActivate
    WinMove A,, 0, 0, A_ScreenWidth/3, A_ScreenHeight/2-20
    }
If (MyVar = "2") {
    WinActivate
    WinMove A,, 0, A_ScreenHeight/2-20, A_ScreenWidth/3, A_ScreenHeight/2-20
    }
If (MyVar = "3") {
    WinActivate
    WinMove A,, A_ScreenWidth/3, 0, A_ScreenWidth/3, A_ScreenHeight/2-20
    }
If (MyVar = "4") {
    WinActivate
    WinMove A,, A_ScreenWidth/3, A_ScreenHeight/2-20, A_ScreenWidth/3, A_ScreenHeight/2-20
    }

If (MyVar = "0") {
    WinActivate
    WinMove A,, A_ScreenWidth*2/3, 0, A_ScreenWidth/3, A_ScreenHeight-40
    }
return