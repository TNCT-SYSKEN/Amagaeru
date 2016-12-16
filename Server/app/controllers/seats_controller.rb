class SeatsController < ApplicationController
  def index
    if user_params.include?("depertment") && user_params.include?("grade")
      @m = user_params["depertment"].empty? || user_params["grade"].empty? ? "Error: Invalid Parameters" : user_params["depertment"] + "科" + user_params["grade"] + "年"
      @seat = Seat.where("depertment = ? AND grade = ?", user_params["depertment"], user_params["grade"]).first
    else
      @m = "Please select depertment and grade"
    end
  end
  private
  def user_params
    params
  end
end
