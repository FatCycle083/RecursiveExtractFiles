import os
import glob
import traceback
import shutil
import sys

from CustomMessageBox import CustomMessageBox
from CustomMessageBox import SelectResult

class RecursiveExtractFileToolsClass():
	
	"""定数"""
	APP_VERSION = "20250310_1"

	def __init__(self, *args:tuple, **kwargs:dict, ):
		"""_summary_
		コンストラクタ
		"""
		print(f"AppVersion：{self.APP_VERSION}")
		self.recursive_extract_file( *args )

		print( f"処理が終了しました" )
		print( f"Enterで終了します" )
		input()

	"""公開関数"""
	def recursive_extract_file( cls, *args:tuple, ):
		# 引数チェック
		if type(args) != tuple:
			raise ValueError("引数がtupleでは無い")
		
		try:
			moved_file_existed = None

			# 1引数チェック
			for arg in args:

				# 1引数値チェック
				if type(arg) != str:
					print( f"非文字列：{arg}" )
					continue
				if not os.path.isdir( arg ):
					print( f"不明な文字列：{arg}" )
					continue

				# 1フォルダ処理
				try:
					# 検索フォルダ表示
					parent_dir_path:str = arg
					print(f"SearchPath：")

					# エスケープシーケンス回避
					search_glob_str = glob.escape( parent_dir_path )
					print(f"SearchPath(Escaped)：{search_glob_str}")
					
					# ファイル検索文字列作成
					search_glob_str:str = os.path.join( search_glob_str, "**", "*" )
					print(f"SearchGlobRegex：{search_glob_str}")

					# ファイル検索
					found_pathes:list[str] = glob.glob( search_glob_str, recursive=True, )
					found_pathes = [ found_path for found_path in found_pathes if os.path.isfile(found_path) and os.path.dirname(found_path)!=parent_dir_path ]
					print(f"Found：{len(found_pathes)}")

					# 検索結果のファイル郡を移動
					found_file_path:str
					for idx,found_file_path in enumerate(found_pathes, 1):
						print(f"{idx}/{len(found_pathes)} {found_file_path}")

						# 移動先チェック
						found_file_name:str = os.path.basename( found_file_path, )
						move_file_path:str = os.path.join( parent_dir_path, found_file_name )
						if os.path.isfile( move_file_path ):
							select = None
							if moved_file_existed == None:
								select = CustomMessageBox.askyesnoallyesallnocancel( showmsg=f"移動先に同名のファイルが既に存在します\n上書きしますか？\n{found_file_path}\n↓\n{move_file_path}" )
								if select == None or select == SelectResult.RESULT_CANCEL:
									print("選択拒否/選択キャンセル")
									return
								if select == SelectResult.RESULT_ALL_YES or select == SelectResult.RESULT_ALL_NO:
									moved_file_existed = select
							if moved_file_existed == SelectResult.RESULT_ALL_NO or select == SelectResult.RESULT_NO:
								continue
							elif moved_file_existed == SelectResult.RESULT_ALL_YES or select == SelectResult.RESULT_YES:
								os.remove( move_file_path )
								print(f"ファイル削除({move_file_path})")
						try:
							shutil.copy( found_file_path, move_file_path, )
							print(f"ファイルコピー({found_file_path}->{move_file_path})")
						except:
							print("コピーエラー")
							if os.path.isfile( move_file_path ):
								os.remove( move_file_path )
								print(f"ファイル削除({move_file_path})")
							traceback.print_exc()
						else:
							os.remove( found_file_path )
							print(f"ファイル削除({found_file_path})")

				except:
					traceback.print_exc()
					return False


		except:
			print("想定外エラー")
			traceback.print_exc()

RecursiveExtractFileToolsClass( *(sys.argv[1:]) )