class RenameDepartment < ActiveRecord::Migration
  def change
    rename_column :students, :department, :department
    # rename_column :seats, :department, :department
    # rename_column :attendances, :department, :department
    # rename_column :timetables, :department, :department

  end
end
