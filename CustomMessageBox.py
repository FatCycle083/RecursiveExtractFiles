import tkinter as tk
from functools import partial
from enum import Enum

class SelectResult( Enum ):
	"""_summary_
	"""
	RESULT_YES:str		 = "はい"
	RESULT_ALL_YES:str	 = "すべてはい"
	RESULT_NO:str		 = "いいえ"
	RESULT_ALL_NO:str	 = "すべていいえ"
	RESULT_CANCEL:str	 = "キャンセル"


class CustomMessageBox():
	"""_summary_
	"""

	"""定数"""

	"""コンストラクタ"""
	def __init__(self):
		"""_summary_
		コンストラクタ
		"""
		# print( f"選択結果={self.askyesnoallyesallnocancel('テスト')}" )
		pass

	@classmethod
	def askyesnoallyesallnocancel( cls, showmsg:str, dialogtitle:str="確認", ) -> SelectResult:
		"""_summary_
		はい/いいえ/すべてはい/すべていいえ/キャンセルを問うメッセージボックスを表示する

		note:
			ブロッキング
		"""

		# 引数チェック
		if type(showmsg) != str:
			raise ValueError()
		
		# GUI表示
		btndata = [	( SelectResult.RESULT_YES.value,	SelectResult.RESULT_YES,	(0,0), ),
					( SelectResult.RESULT_ALL_YES.value,SelectResult.RESULT_ALL_YES,(0,1), ),
					( SelectResult.RESULT_NO.value,		SelectResult.RESULT_NO,		(1,0), ),
					( SelectResult.RESULT_ALL_NO.value,	SelectResult.RESULT_ALL_NO,	(1,1), ),
					( SelectResult.RESULT_CANCEL.value,	SelectResult.RESULT_CANCEL,	(0,2), ),	]
		return cls._showwidget(	title=dialogtitle,
								lbltxt=showmsg,
								btndatas=btndata,)

	@classmethod
	def _showwidget( cls, title:str, lbltxt:str, btndatas:list[tuple[str,any,tuple[int,int]]], ) -> any:
		"""_summary_
		指定された引数でGUIを作成し返却する

		note:
			ブロッキング
		"""
		btndataslength = 3
		gridtuplelength = 2
		btns_move_x = 0
		btns_move_y = 1
		padding_x = 5
		padding_y = 5
		retval = None

		# 引数チェック
		if type( title ) != str or \
		   type( lbltxt ) != str or \
		   type( btndatas ) != list:
			raise ValueError()

		# 新しいウィンドウを作成
		top = tk.Tk()
		top.title(title)
		top.resizable(False,False)
		top.minsize(300,0)

		# ボタンの応答処理
		def on_button_click( btnsetval:any, ):
			nonlocal retval
			retval = btnsetval
			print("選択：",btnsetval)
			top.destroy()

		# GUI作成
		maxgrid_x:int = 0
		maxgrid_y:int = 0

		# GUI作成(ボタン配置)
		btndata:tuple
		for btndata in btndatas:
			# データチェック
			if type( btndata ) != tuple or len( btndata ) != btndataslength:
				raise ValueError( btndata )
			btntxt:str
			btnreturn:any
			btngridpos:tuple
			btntxt, btnreturn, btngridpos = btndata
			if type( btntxt ) != str or \
			type( btngridpos ) != tuple or \
			len( btngridpos ) != gridtuplelength:
				raise ValueError( type(btntxt), type(btngridpos), btngridpos )
			btngrid_x:int
			btngrid_y:int
			btngrid_x,btngrid_y = btngridpos
			maxgrid_x = max( btngrid_x, maxgrid_x )
			maxgrid_y = max( btngrid_y, maxgrid_y )

			btn = tk.Button(top, text=btntxt, command=partial(on_button_click,btnreturn), )
			btn.grid( column=btngrid_x+btns_move_x, row=btngrid_y+btns_move_y, sticky=tk.NSEW, padx=padding_x, pady=padding_y, )

		label = tk.Label(top, text=lbltxt, padx=padding_x, pady=padding_y, anchor=tk.W, )
		label.grid( column=0, row=0, sticky=tk.NSEW, columnspan=maxgrid_x+1, )
		top.grid_columnconfigure( list(range(maxgrid_x+1)), weight=1, uniform="column" )

		# GUI表示
		top.mainloop()
		return retval
