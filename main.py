import model
import Presenter
import View

model = model.MinesweeperModel()
controller = Presenter.MinesweeperController(model)
view = View.MinesweeperView(model, controller)
view.pack()
view.mainloop()