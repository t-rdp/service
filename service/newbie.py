from service import route
from service.middleware import authRequired
from flask import request, render_template
import json
import misc
import misc.note
import misc.misskey
import misc.hcaptcha

@route.route("/newbie", methods=["GET"])
@authRequired()
def newbie(*, id, ud):
    questions = json.load(open("questions.json", encoding="utf-8"))
    return render_template("newbie.html", questions=questions, ud=ud)

@route.route("/newbie", methods=["POST"])
@authRequired()
def newbie_post(*, id, ud):
    questions = json.load(open("questions.json", encoding="utf-8"))
    hcr = request.form.get("h-captcha-response", "")
    if not misc.hcaptcha.check(hcr):
        return misc.note.create_note("人机验证失败！<a href='/platform/newbie'>重新考试</a>。")
    questions_correct = []
    questions_submit = []
    questions_score = 0
    questions_min_score = questions["correct"]
    questions_length = questions["length"]
    for q in range(questions_length):
        questions_correct.append(str(questions[str(q)]["correct"]))
        questions_submit.append(str(request.form.get("q_" + str(q), "0")))
        if str(questions[str(q)]["correct"]) == str(request.form.get("q_" + str(q), "0")): questions_score += 1
    if questions_score >= questions_min_score:
        misc.misskey.misskey_post("admin/roles/assign", {"userId": id, "roleId": misc.config["misskey"]["nb_role"], "expiresAt": None})
        return misc.note.create_note("转正成功！您的分数为：" + str(questions_score) + "，<a href='/@" + ud["username"] + "'>查看您的个人主页</a>。")
    else:
        return misc.note.create_note("转正失败！您的分数为：" + str(questions_score) + "，离成功只差 " + str(questions_min_score - questions_score) + " 分，<a href='/platform/newbie'>再次尝试</a>。")