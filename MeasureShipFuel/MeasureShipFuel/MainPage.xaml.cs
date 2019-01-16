using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Forms;

namespace MeasureShipFuel
{
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            InitializeComponent();
        }

        private void Predict_Volume(object sender, EventArgs e)
        {
            Navigation.PushAsync(new PredictVolume());
        }

        private void New_Measurement(object sender, EventArgs e)
        {
            Navigation.PushAsync(new NewMeasurement());
        }
    }
}
