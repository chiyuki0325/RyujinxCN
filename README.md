# RyujinxCN
自制 Ryujinx GTK UI 汉化版

如何使用：

- 克隆 Ryujinx 的 git 仓库
- `python3 localization.py Ryujinx`
- 之后编译即可

```bash
git clone https://github.com/Ryujinx/Ryujinx.git
python3 ./localization.py Ryujinx
cd Ryujinx
dotnet publish -c Release -p:DebugType=embedded Ryujinx --self-contained true
```

Arch Linux 用户可以直接使用 PKGBUILD
