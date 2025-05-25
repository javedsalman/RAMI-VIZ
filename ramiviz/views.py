import os
import json
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Import algorithms
from scripts import alg1, alg2, alg3, alg4, alg5, alg6, alg7

def home(request):
    return render(request, 'index.html')

@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('input_file'):
        input_file = request.FILES['input_file']
        filename = default_storage.save(os.path.join('uploads', input_file.name), input_file)
        file_path = os.path.join(settings.MEDIA_ROOT, filename)

        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
        except Exception as e:
            return JsonResponse({'error': f'Invalid JSON: {str(e)}'}, status=400)

        # Run Algorithm 1: Preprocessing
        validated, validation_errors = alg1.run(data)

        # Run Algorithm 2: RAMI Mapping
        mapped = alg2.run(validated)

        # Run Algorithm 3: Workflow filtering (default = all 'machine_data')
        workflow_services = ['machine_data']
        filtered = alg3.run(mapped, workflow_services)

        # Run Algorithm 4: Interaction matrix and clustering
        interaction_result = alg4.run(filtered)
        clusters = interaction_result['clusters']

        # Run Algorithm 5: 3D point mapping
        spatial_data = alg5.generate_3d_points(filtered, clusters)

        # Run Algorithm 6: Value addition projection
        value_projection = alg6.run(filtered)

        # Run Algorithm 7: Lifecycle phase mapping
        lifecycle_map = alg7.run(filtered)

        return JsonResponse({
            'status': 'success',
            'validation_errors': validation_errors,
            'spatial_data': spatial_data,
            'value_projection': value_projection,
            'lifecycle_timeline': lifecycle_map
        })

    return JsonResponse({'error': 'Invalid request.'}, status=400)
