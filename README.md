# RecursiveExtractFiles
指定されたフォルダパスに含まれる全てのファイルを指定されたフォルダパス直下に移動させる

# 使い方( How To Use? )
引数にフォルダパスを付けて実行する

# おすすめ( Recommendation )
レジストリに登録し、エクスプローラーでフォルダを右クリックしたときにメニュー表示する  
1. PyInstallerでexe化

1. 任意のフォルダに配置し、exeのファイルパスを控える

1. レジストリエディタで下記の箇所に任意の名前でキーを作成する  
HKEY_CLASSES_ROOT\Directory\Background\shell  
HKEY_CLASSES_ROOT\Directory\shell  
※右クリックメニューに表示されるため、ソフトウェア名を識別可能な文字列を推奨  
※※表示したいテキストがキー名に相応しくない場合、作成したキー内の **(規定)** の値を表示したいテキストに変更する

1. 作成したキー名の下に **command** という名前で再度キーを作成

1. 作成した **command** キー内の **(規定)** のデータを修正し、  
**"exeファイルのフルパス" "%V"** といった値に変更する  
![最終的なレジストリのサンプル画像](https://github.com/FatCycle083/RecursiveExtractFiles/blob/main/ReadMe_Imgs/RegistryEditorImg.jpg?raw=true)

1. PCの再起動を行う  
![レジストリ登録時のサンプル画像](https://github.com/FatCycle083/RecursiveExtractFiles/blob/main/ReadMe_Imgs/WindowsSample.jpg?raw=true)
