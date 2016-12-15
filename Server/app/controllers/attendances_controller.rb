class AttendancesController < ApplicationController
    def index
      depertment = user_params["depertment"] || "C"
      grade = user_params["grade"] || 1
      @date = user_params.include?("date") && user_params["date"].empty? ? '2016-04-04' : user_params["date"]
      @mode = user_params["mode"] || "office"

      if @mode == "teacher"
          @subjectAttendance = SubjectAttendance.where("subject_id = ?", user_params["subject"]).first
      elsif @mode == "office"
          @all = DayAttendance.where("date between ? and ?", @date, (@date.to_date + 5).to_s).order("date")
          @dayAttendances = []
          5.times do |n|
            @dayAttendances[n] = @all.where("date = ?", (@date.to_date + n).to_s)
          end
      end
    end

    private
      def user_params
        params
      end
end
