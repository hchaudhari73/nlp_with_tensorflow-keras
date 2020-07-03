import matplotlib.pyplot as plt

def plots(model):
    plt.plot(model.history.history["loss"], label="Loss")
    plt.plot(model.history.history["val_loss"], label="Validation Loss")
    plt.legend()
    plt.show()

    plt.plot(model.history.history["accuracy"], label="Accuracy")
    plt.plot(model.history.history["val_accuracy"], label="Validation Accuracy")
    plt.legend()
    plt.show()
