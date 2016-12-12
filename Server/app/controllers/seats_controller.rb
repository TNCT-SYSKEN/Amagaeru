class SeatsController < ApplicationController
  def index
    if user_params.include?("department") && user_params.include?("gread")
      @m = user_params["department"].empty? || user_params["gread"].empty? ? "Error: Invalid Parameters" : user_params["department"] + "科" + user_params["gread"] + "年"
      @seat = Seat.where("department = ? AND gread = ?", user_params["department"], user_params["gread"]).first
    else
      @m = "Please select depertment and grade"
    end
  end
  private
  def user_params
    params
  end
end
