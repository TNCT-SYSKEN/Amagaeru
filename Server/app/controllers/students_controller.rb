class StudentsController < ApplicationController
  def index
    @m = user_params["depertment"].empty? || user_params["grade"].empty? ?  "Error: Invalid Parameters" : user_params["depertment"] + "科" + user_params["grade"] + "年"
    @students = Student.where("depertment = ? AND grade = ?", user_params["depertment"], user_params["grade"])
  end

  private
    def user_params
      params
    end
end
