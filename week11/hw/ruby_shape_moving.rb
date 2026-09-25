# Acknowledgement to the original authors of the code on which this
# example is based.
require 'gosu'

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 400

class GameWindow < Gosu::Window
  def initialize
    super(SCREEN_WIDTH, SCREEN_HEIGHT)
    self.caption = "Gosu Example"

    @done = false
    @is_blue = true
    @x = 30
    @y = 30

    @size = 60   # NEW: size of square
  end

  def update
    close if @done 

    # LEFT / RIGHT
    @x -= 3 if button_down?(Gosu::KB_LEFT)
    @x += 3 if button_down?(Gosu::KB_RIGHT)

    #  NEW: UP / DOWN
    @y -= 3 if button_down?(Gosu::KB_UP)
    @y += 3 if button_down?(Gosu::KB_DOWN)

    #  KEEP INSIDE WINDOW
    @x = 0 if @x < 0
    @y = 0 if @y < 0

    @x = SCREEN_WIDTH - @size  if @x + @size > SCREEN_WIDTH
    @y = SCREEN_HEIGHT - @size if @y + @size > SCREEN_HEIGHT

    puts "x is #{@x} y is #{@y} size is #{@size}"
  end

  def draw
    Gosu.draw_rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, Gosu::Color::BLACK)

    if @is_blue
      color = Gosu::Color.rgb(0, 128, 255)
    else
      color = Gosu::Color.rgb(255, 100, 0)
    end
    Gosu.draw_rect(@x, @y, @size, @size, color)
  end

  def button_down(id)
    if id == Gosu::KB_ESCAPE
      @done = true
    end

    # toggle color
    if id == Gosu::KB_SPACE
      @is_blue = !@is_blue 
    end

    #  BONUS: resize
    if id == Gosu::KB_W
      @size += 5 if @size < 120
    end

    if id == Gosu::KB_Q
      @size -= 5 if @size > 0
    end
  end
end

window = GameWindow.new
window.show