from flask import make_response, request, jsonify 
from appFolder import app

data = {"projects":[]}

testP = [
	{
		"nm": "The Dashboard Project",
		"dsc": "Monitor Expenditures",
		"field":[{"nm":"Manger", "dsc":"", "vl":"Somebody"}, {"nm":"Expected Completion Date Long Field", "dsc":"", "vl":"Yesterday"}],
		"note":[
			{
				"dt":123456,
				"txt":"was approved by Joe",
				"usr":"j.smith"
			}
		],
		"milestone":[
			{
				"nm":"Standardize Intake Form",
				"dsc": "Inorder to collect data from all places in a standardized way",
				"field":[{"nm":"manger", "dsc":"", "vl":"George Petterson"}],
				"note":[{"dt":123456, "txt":"waiting on approval of final intake fields", "usr":"G.Petterson"}],
				"task":[]
			}
		],
	},
	{
		"nm": "Different Dashboard",
		"dsc": "Safety First",
		"field":[{"nm":"Manger", "dsc":"", "vl":"Somebody Else"},{"nm":"Mandatory Deadline", "dsc":"", "vl":"Next Week!"}],
		"note":[
			{
				"dt":123456,
				"txt":"was approved by Tom",
				"usr":"j.smith"
			},
			{
				"dt":3456789,
				"txt":"The last step to finish this is hinging on SQL DBA finishing the nested inner join",
				"usr":"j.smith"
			}

		],
		"milestone":[
			{
				"nm": "Some Analysis",
				"dsc": "Leverage Some Data To Identify Concern Areas",
				"field":[{"nm":"asdf"},{"nm":"qwer"}], 
				"note":[
					{
						"dt":123456, 
						"txt":"Steve said we should focus on XYZ", 
						"usr":"j.smith"
					},
					{
						"dt":345678, 
						"txt":"We found good stuff in XYZ, this milestone is complete", 
						"usr":"j.smith"
					}
				], 
				"task":[
					{
						"nm": "Get data",
						"dsc": "ABC and DEF are the main sources, etc",					
						"field":[], 
						"note":[
							{
								"dt":123456, 
								"txt":"I got the data but there is garbage in it so need to write a python script that will clean it", 
								"usr":"j.smith"
							},
							{
								"dt":456789, 
								"txt":"cleaned the data, python script works, not very robust but did the job.  Data is ready for analysis/dashboarding", 
								"usr":"j.smith"
							}
						]
					}
				]
			}
		]
	}
]


@app.route('/')
def ui(page=None):
	return make_response(open('appFolder/index.html').read())

@app.route('/api/test')
def test():
	return jsonify(data=testP)


@app.route('/api/project', methods=['GET','POST'])
def api_project():
	if request.method == 'GET':
		return jsonify(data)
	if request.method =='POST':
		data["projects"].append(request.json)
		return "flask POST"

@app.route('/api/milestone', methods=['GET','POST'])
def api_milestone():
	if request.method == 'GET':
		return jsonify(data)
	if request.method =='POST':
		req = request.json
		for p in data["projects"]:
			if p['name'] == req['p_name']:
				req.pop('p_name')
				if 'milestones' in p: 
					p['milestones'].append(req)
				else:
					p['milestones'] = [req]
		print(data)
		return "flask POST"


