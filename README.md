# Python 基本講座
LinkedInラーニングの「Python 基本講座」コース用のリポジトリです。このコースは[LinkedInラーニング][lil-course-url]で視聴できます。

![lil-thumbnail-url]

PythonはAI活用や機械学習の分野を中心に、今や世界中でもっとも注目されているプログラミング言語のひとつです。文法がシンプルなので、読みやすくて書きやすい、学習コストの低いプログラミング言語として学生やプログラマーでない人の間でも利用が広まっています。Pythonにはプログラムの作成を助ける豊富なライブラリがあり、ゲームやサーバー管理、アプリ開発や機械学習、AI活用など応用範囲が広いのも特徴です。このコースではPythonを使ったプログラミングの基本を学びます。Pythonの特徴はもちろん、関数や変数などの基本構文、リストや文字列といったイテラブルオブジェクトの操作、オブジェクト指向プログラミング、またORMライブラリを使ってデータベースを扱う方法にも触れます。このコースでPythonのプログラミングの基礎を身につけましょう。

## リポジトリの使い方
このリポジトリには必要に応じてブランチが設けられています。ブランチのポップアップメニューを使用して、使用するブランチに切り替えたあとにコースを視聴してください。またURLに`「/tree/ブランチ名」`を追加することで、アクセスしたいブランチに移動することも可能です。

## ブランチ
ブランチはレッスンごとに作成されている場合があります。その場合はブランチ名に`「章番号_レッスン番号」`が付けられています。例えば`「02_03」`という名前のブランチは、2章の上から3番目のレッスン用のブランチとなります。

レッスン前と後のコードを格納しているブランチもあります。該当ブランチには「開始時」（beginning）を表す`「b」`と、「終了時」（ending）を表す`「e」` がブランチ名についています。`「b」`のブランチにはレッスン開始時点のコードが、`「e」`のブランチにはレッスン終了時点のコードが格納されています。また「main」のブランチにはコードの最終形が格納されています。

ファイルに変更を加えた後に、エクササイズファイルのブランチを次のブランチに切り替えたさい、次のようなメッセージが表示されることがあります。

    error: Your local changes to the following files would be overwritten by checkout:        [files]
    Please commit your changes or stash them before you switch branches.
    Aborting

この問題を解決するには：
	
    次のコマンドで変更を加えます：git add .
	次のコマンドで変更をコミットします：git commit -m "some message"
 
 ## GitHub Codespacesについて
プログラミング言語を学ぶ最良の方法は、実際にそれを使用することです。それがこのコースがGitHub Codespacesと統合されている理由です。GitHub Codespacesは、あなたが普段使っているIDEのすべての機能を提供するクラウド上の手軽な開発環境です。ローカルマシンのセットアップも必要ありません。 GitHub Codespacesを使えば、あなたが職場で使っている他のツールを使用しながら、どのパソコンからでもいつでもプログラミングの実践的な練習ができます。

### インストラクター

金宏和實
                            
株式会社イーザー副社長、テクニカルライター

[0]: # (Replace these placeholder URLs with actual course URLs)

[lil-course-url]: https://www.linkedin.com/learning/python-essential-training-2026
[lil-thumbnail-url]: https://media.licdn.com/dms/image/v2/D560DAQHtS4-dZZEKTg/learning-public-crop_675_1200/B56Z1pWYLAJkAc-/0/1775588967357?e=2147483647&v=beta&t=n89eaAG2XnUzBL1QqNVM8Mq429tKI5Kyo6d17xwKmnE
