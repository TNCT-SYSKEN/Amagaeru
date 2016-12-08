class CreateStudents < ActiveRecord::Migration
  def change
    create_table :students do |t|
      t.string :depertment
      t.integer :grade
      t.integer :number
      t.string :first_name #名前
      t.string :last_name #苗字

      t.timestamps null: false
    end
  end
end
