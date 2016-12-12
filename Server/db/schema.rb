# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20161212081604) do

  create_table "seat_data", force: :cascade do |t|
    t.integer  "number"
    t.string   "first_name"
    t.string   "last_name"
    t.integer  "seat_line_id"
    t.datetime "created_at",   null: false
    t.datetime "updated_at",   null: false
  end

  add_index "seat_data", ["seat_line_id"], name: "index_seat_data_on_seat_line_id"

  create_table "seat_lines", force: :cascade do |t|
    t.integer  "line_no"
    t.integer  "seat_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  add_index "seat_lines", ["seat_id"], name: "index_seat_lines_on_seat_id"

  create_table "seats", force: :cascade do |t|
    t.string   "department"
    t.integer  "grade"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "students", force: :cascade do |t|
    t.string   "depertment"
    t.integer  "grade"
    t.integer  "number"
    t.string   "first_name"
    t.string   "last_name"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

end
