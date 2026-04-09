from tensorflow.keras.optimizers import Adam, RMSprop, SGD

def compile_model(model, optimizer_name="adam"):
    if optimizer_name == "adam":
        opt = Adam(learning_rate=0.001)
    elif optimizer_name == "rmsprop":
        opt = RMSprop(learning_rate=0.001)
    else:
        opt = SGD(learning_rate=0.001)

    model.compile(
        loss="sparse_categorical_crossentropy",
        optimizer=opt,
        metrics=["accuracy"]
    )

    return model