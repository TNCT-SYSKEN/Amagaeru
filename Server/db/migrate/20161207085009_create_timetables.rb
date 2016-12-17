class CreateTimetables < ActiveRecord::Migration
  def change
    create_table :timetables do |t|
      t.string :department
      t.integer :grade

      t.timestamps null: false
    end
  end
end
