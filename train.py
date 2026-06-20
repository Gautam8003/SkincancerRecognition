from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense

train = ImageDataGenerator(
    rescale=1./255
)

data = train.flow_from_directory(

    "dataset/train",

    target_size=(128,128),

    batch_size=32,

    class_mode="binary"
)

model = Sequential()
model.add(Input(shape=(128, 128, 3)))
model.add(
    Conv2D(
        32,
        (3, 3),
        activation="relu"
    )
)

model.add(MaxPooling2D())
model.add(Flatten())

model.add(
Dense(
64,
activation="relu"
)
)

model.add(
Dense(
1,
activation="sigmoid"
)
)

model.compile(
optimizer="adam",
loss="binary_crossentropy",
metrics=["accuracy"]
)

model.fit(
data,
epochs=5
)

model.save(
"models/skin_model.h5"
)

print("Training Complete")