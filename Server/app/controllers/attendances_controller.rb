class AttendancesController < ApplicationController
    def index
      if user_params.include?("depertment") && user_params.include?("grade") && user_params.include?("subject")
        @m = user_params["depertment"].empty? || user_params["grade"].empty? || user_params["subject"].empty? ?  "Error: Invalid Parameters" : user_params["depertment"] + "科" + user_params["grade"] + "年 " + Subject.where("id = ?", user_params["subject"]).first.name
        @subjectAttendance = SubjectAttendance.where("subject_id = ?", user_params["subject"]).first
      else
        @m = "Please select depertment, grade and subject"
      end
    end

    private
      def user_params
        params
      end
end
