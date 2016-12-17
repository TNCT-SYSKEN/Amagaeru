class CreateStudentStatuses < ActiveRecord::Migration
  def change
    create_table :student_statuses do |t|
      t.integer :student_id
      t.integer :day_attendance_id
      t.integer :status

      t.timestamps null: false
    end
  end
end
