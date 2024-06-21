import geojson
import os

class FeatureCollection:

    @staticmethod
    def create_feature_collection(coordinates):
        # Create a FeatureCollection
        features = []
        for coord in coordinates:
            point = geojson.Point((coord["lng"], coord["lat"]))
            feature = geojson.Feature(geometry=point, properties={})
            features.append(feature)

        feature_collection = geojson.FeatureCollection(features)
        return feature_collection

    @staticmethod
    def write_geojson(feature_collection):
        # Save to a GeoJSON file
        geofile_out = os.path.join('data', 'points.geojson')
        with open(geofile_out, 'w') as f:
            geojson.dump(feature_collection, f, indent=2)

    
if __name__ == '__main__':
    # List of coordinates
    coordinates = [
        {"lat": 40.7128, "lng": -74.0060},
        {"lat": 34.0522, "lng": -118.2437},
        {"lat": 37.7749, "lng": -122.4194}
    ]
    feature_col = FeatureCollection.create_feature_collection(coordinates)
    FeatureCollection.write_geojson(feature_col)
        
    print("GeoJSON file created successfully!")
