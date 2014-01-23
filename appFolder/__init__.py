from flask import Flask

# configuration
DATABASE = 'theDataBase.db'
DEBUG = True
SECRET_KEY = '1234'


#create our little application :)
app = Flask(__name__)

app.config['DATABASE'] = DATABASE
app.config['DEBUG'] = DEBUG
app.config['SECRET_KEY'] = SECRET_KEY

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



#this import is neccesary even though it doesn't look like it is being used
import appFolder.views
