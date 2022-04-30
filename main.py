from flask import Flask, render_template

import utils


app = Flask(__name__)


@app.route("/")
def list_candidates():
    candidates = utils.load_candidates_from_json("candidates.json")
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:candidate_id>")
def card_candidate(candidate_id):
    candidate = utils.get_candidate(candidate_id)
    return render_template("card.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def search_candidate(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates, candidates_count=len(candidates))


@app.route("/skill/<skill_name>")
def skill_candidate(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template("skill.html", candidates=candidates, candidates_count=len(candidates))


app.run()
