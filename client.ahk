MyVar = %2%
MyVar2 = %1%
Run cmd.exe
Sleep, 1000
Send, client.py %1%

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