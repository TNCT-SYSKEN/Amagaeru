class StudentsController < ApplicationController
  def index
    if user_params.include?("department") && user_params.include?("grade")
      @m = user_params["department"].empty? || user_params["grade"].empty? ?  "Error: Invalid Parameters" : user_params["department"] + "科" + user_params["grade"] + "年"
    else
      @m = "Please select department and grade"
    end
    @students = Student.where("department = ? AND grade = ?", user_params["department"], user_params["grade"])
  end

  private
    def user_params
      params
    end
end
