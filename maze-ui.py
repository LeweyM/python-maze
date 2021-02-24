from browser import document
from browser import html
from browser import aio

from Grid import Grid
from Solver import Solver

div = html.DIV()
animation_is_running = False


async def animate(grid):
    global ctx, animation_is_running
    animation_is_running = True
    solver = Solver(grid)
    while not grid.finished():
        blank_screen(ctx)
        grid.update()
        grid.show()
        await aio.sleep(0.001)
    while not solver.finished:
        blank_screen(ctx)
        solver.update()
        solver.show_visited_nodes()
        grid.show()
        await aio.sleep(0.01)
    solver.show_trail()
    grid.show()
    animation_is_running = False
    message_to_screen(ctx, "click to restart")


def blank_screen(context):
    context.fillStyle = "black"
    context.fillRect(0, 0, 300, 300)


def message_to_screen(context, msg):
    context.fillStyle = "black"
    context.fillRect(100, 130, 100, 35)
    context.textAlign = "center"
    context.fillStyle = "white"
    context.fillText(msg, 150, 150)


def start_animation(e):
    if not animation_is_running:
        grid = Grid(300, 10, ui)
        aio.run(animate(grid))


class UI:
    def __init__(self, cnv):
        self.cnv = cnv

    def line(self, color, start, end):
        self.cnv.strokeStyle = color
        self.cnv.lineCap = "round"
        self.cnv.lineWidth = 3
        self.cnv.beginPath()
        self.cnv.moveTo(start[0], start[1])
        self.cnv.lineTo(end[0], end[1])
        self.cnv.stroke()

    def rect(self, color, rect):
        x, y, w, h = rect
        self.cnv.fillStyle = color
        self.cnv.fillRect(x, y, w, h)


canvas = html.CANVAS(width=300, height=300)
ctx = canvas.getContext('2d')
blank_screen(ctx)
message_to_screen(ctx, "click to start")
canvas.bind("click", start_animation)

ui = UI(ctx)

div <= canvas

document <= div
