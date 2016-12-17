class AttendancesController < ApplicationController
    def index
      depertment = user_params["depertment"].blank? ? "C" : user_params["depertment"]
      grade = (user_params["grade"].blank? ? 1 : user_params["grade"]).to_s
      @week = (user_params["week"].blank? ? 14 : user_params["week"]).to_i
      @mode = user_params["mode"].blank? ? "office" : user_params["mode"]

      attendance_id = Attendance.where("depertment = ? and grade = ?", depertment, grade).first ? Attendance.where("depertment = ? and grade = ?", depertment, grade).first.id : 0

      if @mode == "teacher"
        @subjectAttendance = SubjectAttendance.where("subject_id = ? and attendance_id = ?", user_params["subject"], attendance_id).first
        @message = depertment + "科" + grade + "年 " + @subjectAttendance.subject.name
      elsif @mode == "office"
        @dayAttendances = DayAttendance.where("attendance_id = ? and date between ? and ?", attendance_id, (Date.commercial(2016, @week)).to_s, (Date.commercial(2016, @week) + 5).to_s)
        @message = depertment + "科" + grade + "年" + " 第" + @week.to_s + "週"
      end
    end

    private
      def user_params
        params
      end
end
