param()
$size = (dir choose-your-own-adventure.phext).Length
$size = [Math]::Round($size/1024/102.4)/10
"$size MiB"