import random
def lambda_handler(event, context):
    adjectives = ["adaptable", "adventurous", "affectionate", "ambitious", "amiable", "compassionate", "considerate", "courageous", "courteous", "diligent", "empathetic", "exuberant", "frank", "generous", "gregarious", "impartial", "intuitive", "inventive", "passionate", "persistent", "philosophical", "practical", "rational", "reliable", "resourceful", "sensible", "sincere", "sympathetic", "unassuming", "witty"]
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
        },
        'body': "{} the {}".format(event['queryStringParameters']['name'], random.choice(adjectives)).title()
    }
