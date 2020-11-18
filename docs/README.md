# ドキュメント管理

`tigerfish/docs` 以下に配布するドキュメントを保存してください。  
## LaTeXのコンパイル

`.tex` 形式のソースコードが記録されていますが、これをPDFにするにはコンパイル作業が必要です。
事前にLaTeXのコンパイラを入手し、

```sh
$ platex main.tex
$ pbibtex main
$ dvipdfmx main
```

を実行すればコンパイルされます。

