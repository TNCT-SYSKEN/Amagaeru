class AttendancesController < ApplicationController
    def index
      department = user_params["department"].blank? ? "C" : user_params["department"]
      grade = (user_params["grade"].blank? ? 1 : user_params["grade"]).to_s
      @week = (user_params["week"].blank? ? 14 : user_params["week"]).to_i
      #$mode = user_params["mode"].blank? ? "office" : user_params["mode"]

      attendance_id = Attendance.where("department = ? and grade = ?", department, grade).first ? Attendance.where("department = ? and grade = ?", department, grade).first.id : 0

      if $mode == "teacher"
        if(!(user_params["subject"].blank?))
          @subjectAttendance = SubjectAttendance.where("subject_id = ? and attendance_id = ?", user_params["subject"], attendance_id).first
          @message = department + "科" + grade + "年 " + @subjectAttendance.subject.name
        end
      elsif $mode == "office"
        @dayAttendances = DayAttendance.where("attendance_id = ? and date between ? and ?", attendance_id, (Date.commercial(2016, @week)).to_s, (Date.commercial(2016, @week) + 5).to_s)
        @message = department + "科" + grade + "年" + " 第" + @week.to_s + "週"
      end
    end

    def index0
      $mode = "teacher"
      redirect_to attendances_index_path

    end
    def index1
      $mode = "office"
      redirect_to attendances_index_path
    end

    private
      def user_params
        params
      end
      def mode
        mode
      end
end
